from kata import TennisGame,add_score

def test_kata_score_0_0_server_win():
    assert TennisGame.add_score(0,0,0)==(15,0)

def test_kata_score_0_0_receiver_win():
    assert kata.add_score(0,0,1)==(0,15)

def test_kata_score_40_something_server_win():
    assert kata.add_score(40,0,0)==("Win",0)
# server win

def test_kata_score_something_40_receiver_win():
    assert kata.add_score(0,40,1)==(0,"Win")
# receiver win

def test_kata_score_40_40_server_win():
    assert kata.add_score(40,40,0)==("A",40)
# server advantage

def test_kata_score_40_40_receiver_win():
    assert kata.add_score(40,40,1)==(40,"A")
# receiver advantage

def test_kata_score_40_A_server_win():
    assert kata.add_score(40,"A",0)==(40,40)
# deuce

def test_kata_score_A_40_receiver_win():
    assert kata.add_score("A",40,1)==(40,40)
# deuce

def test_kata_score_A_40_sever_win():
    assert kata.add_score("A",40,0)==("Win",40)
# server win
#
def test_kata_score_40_A_receiver_win():
    assert kata.add_score(40,"A",1)==(40,"Win")
# receiver win