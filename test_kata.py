from kata import TennisGame,add_score

def test_kata_score_0_0_server_win():
     assert TennisGame(0,0).add_score(0)==(15,0)

def test_kata_score_0_0_receiver_win():
     assert TennisGame(0,0).add_score(1)==(0,15)

def test_kata_score_40_something_server_win():
     assert TennisGame(40,15).add_score(0)==("Win",15)
# server win

def test_kata_score_something_40_receiver_win():
    assert TennisGame(15,40).add_score(1)==(15,"Win")
# receiver win

def test_kata_score_40_40_server_win():
    assert TennisGame(40,40).add_score(0)==("A",40)
# server advantage

def test_kata_score_40_40_receiver_win():
    assert TennisGame(40,40).add_score(1)==(40,"A")
# receiver advantage

def test_kata_score_40_A_server_win():
    assert TennisGame(40,"A").add_score(0)==(40,40)
# deuce

def test_kata_score_A_40_receiver_win():
    assert TennisGame("A",40).add_score(1)==(40,40)
# deuce

def test_kata_score_A_40_sever_win():
    assert TennisGame("A",40).add_score(0)==("Win",40)
# server win

def test_kata_score_40_A_receiver_win():
    assert TennisGame(40,"A").add_score(1)==(40,"Win")
# receiver win