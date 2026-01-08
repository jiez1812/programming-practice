import sys
sys.path.insert(0,'.')

from solution import authenticate_ad

def test_authenticate_ad_success(mocker):
    mock_conn = mocker.patch('solution.Connection')
    mock_conn.return_value.bound = True

    result = authenticate_ad('fake_url','fake_user','fake_password')

    assert result == True