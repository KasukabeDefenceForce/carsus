import pytest
from numpy.testing import assert_almost_equal
from carsus.alchemy import Atom


def test_atomic_database_init_empty_db(db_session):
    assert db_session.query(Atom).count() == 118


@pytest.mark.parametrize("atomic_number,expected",[
    (1, {'atomic_number':1, 'symbol':'H', 'name':'Hydrogen', 'group': 1.0, 'period':1}),
    (19, {'atomic_number':19, 'symbol':'K', 'name':'Potassium', 'group': 1.0, 'period':4})
])
def test_atomic_database_test_atoms(atomic_number, expected, db_session):
    atom = db_session.query(Atom).filter_by(atomic_number=atomic_number).one()
    assert atom.atomic_number == expected['atomic_number']
    assert atom.symbol == expected['symbol']
    assert atom.name == expected['name']
    assert_almost_equal(atom.group, expected['group'])
    assert atom.period == expected['period']