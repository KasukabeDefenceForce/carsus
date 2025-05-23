import logging

import astropy.constants as const
import pandas as pd

from carsus.io.util import get_lvl_index2id, exclude_artificial_levels

logger = logging.getLogger(__name__)


class CollisionsPreparer:
    def __init__(self, reader):
        collisions = reader.collisions.copy()
        collisions.index = collisions.index.rename(
            [
                "atomic_number",
                "ion_number",
                "level_number_lower",
                "level_number_upper",
            ]
        )

        self.collisions = collisions
        self.collisions_metadata = reader.collisional_metadata

    def prepare_collisions(self):
        """
        Prepare the DataFrame with electron collisions for TARDIS.

        Returns
        -------
        pandas.DataFrame

        """

        collisions_index = [
            "atomic_number",
            "ion_number",
            "level_number_lower",
            "level_number_upper",
        ]

        if "chianti" in self.collisions_metadata.dataset:
            collisions_columns = collisions_index + [
                "e_col_id",
                "lower_level_id",
                "upper_level_id",
                "btemp",
                "bscups",
                "ttype",
                "cups",
                "gf",
                "g_l",
                "energy_lower",
                "g_u",
                "energy_upper",
                "delta_e",
                "g_ratio",
            ]

        elif "cmfgen" in self.collisions_metadata.dataset:
            collisions_columns = collisions_index + list(self.collisions.columns)

        else:
            raise ValueError("Unknown source of collisional data")

        collisions_prepared = (
            self.collisions.reset_index().loc[:, collisions_columns].copy()
        )
        self.collisions_prepared = collisions_prepared.set_index(collisions_index)


class ChiantiCollisionsPreparer(CollisionsPreparer):
    def __init__(
        self,
        chianti_reader,
        levels,
        levels_all,
        lines_all,
        chianti_ions,
    ):
        self.chianti_reader = chianti_reader
        self.levels = levels
        self.levels_all = levels_all
        self.lines_all = lines_all
        self.chianti_ions = chianti_ions

        self.collisions = self.create_chianti_collisions()
        self.collisions_metadata = pd.Series(
            {
                "dataset": ["chianti"],
                "info": None,
            }
        )

    def create_chianti_collisions(self):
        """
        Generates the definitive `collisions` DataFrame by adding new columns
        and making some calculations.

        Returns
        -------
        pandas.DataFrame

        Notes
        -----
        Produces the same output than `AtomData.create_collisions` method.

        """

        logger.info("Ingesting collisional strengths.")
        ch_collisions = self.chianti_reader.collisions
        ch_collisions["ds_id"] = 4

        # Not really needed because we have only one source of collisions
        collisions = pd.concat([ch_collisions], sort=True)
        ions = self.chianti_ions

        collisions = collisions.reset_index()
        collisions = collisions.rename(columns={"ion_charge": "ion_number"})
        collisions = collisions.set_index(["atomic_number", "ion_number"])

        logger.info("Matching collisions and levels.")
        col_list = [
            get_lvl_index2id(collisions.loc[ion], self.levels_all) for ion in ions
        ]
        collisions = pd.concat(col_list, sort=True)
        collisions = collisions.sort_values(by=["lower_level_id", "upper_level_id"])

        # `e_col_id` number starts after the last line id
        start = self.lines_all.index[-1] + 1
        collisions["e_col_id"] = range(start, start + len(collisions))

        # Exclude artificially created levels from levels
        levels = exclude_artificial_levels(self.levels)

        # Join atomic_number, ion_number, level_number_lower, level_number_upper
        collisions = collisions.set_index(["atomic_number", "ion_number"])
        lower_levels = levels.rename(
            columns={
                "level_number": "level_number_lower",
                "g": "g_l",
                "energy": "energy_lower",
            }
        ).loc[
            :,
            [
                "atomic_number",
                "ion_number",
                "level_number_lower",
                "g_l",
                "energy_lower",
            ],
        ]

        upper_levels = levels.rename(
            columns={
                "level_number": "level_number_upper",
                "g": "g_u",
                "energy": "energy_upper",
            }
        ).loc[:, ["level_number_upper", "g_u", "energy_upper"]]

        collisions = collisions.join(lower_levels, on="lower_level_id").join(
            upper_levels, on="upper_level_id"
        )

        # Calculate delta_e
        kb_ev = const.k_B.cgs.to("eV / K").value
        collisions["delta_e"] = (
            collisions["energy_upper"] - collisions["energy_lower"]
        ) / kb_ev

        # Calculate g_ratio
        collisions["g_ratio"] = collisions["g_l"] / collisions["g_u"]

        collisions = collisions.rename(
            columns={"temperatures": "btemp", "collision_strengths": "bscups"}
        )

        collisions = collisions[
            [
                "e_col_id",
                "lower_level_id",
                "upper_level_id",
                "ds_id",
                "btemp",
                "bscups",
                "ttype",
                "cups",
                "gf",
                "atomic_number",
                "ion_number",
                "level_number_lower",
                "g_l",
                "energy_lower",
                "level_number_upper",
                "g_u",
                "energy_upper",
                "delta_e",
                "g_ratio",
            ]
        ]

        collisions = collisions.set_index("e_col_id")

        return collisions
