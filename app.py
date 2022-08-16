from flask import Flask
from flask import render_template
import jyserver.Flask as jsf
from connect4 import NodeConnectFour
from connect4 import Tree

app = Flask(__name__)

@jsf.use(app)
class App:
  def __init__(self):
    self.b_rows = 6
    self.b_cols = 7
    self.initState = [[0 for i in range(self.b_cols)] for j in range(self.b_rows)]
    self.operators = [i for i, f in enumerate(self.initState[0])]
  
  def main_play (self):
    print('se esta jugando desde python')
    state = self.getBoardFromHTML()
    player = self.getPlayerFromHTML()
    pc_play = self.getPCPlay(state, player)
    print('se adquirió la jugada')
    print('la jugada es jugar en la columna: ', pc_play)
    self.placePlayInHTML(pc_play)

    #Click to let know the user we've already played
    self.js.document.getElementById('user_turn').click()

  def getPCPlay (self, state, player):
    nodeJuego = NodeConnectFour(player,value="inicio",state=state, operators=self.operators)
    tree = Tree(nodeJuego, self.operators)
    objective=tree.alpha_beta(3)
    return objective.operator


  def getBoardFromHTML (self):
    playsString = str(self.js.document.getElementById('secret_play_list').innerHTML)
    plays = []

    #Si no hay jugadas registradas
    if len(playsString) == 0:
      return self.initState
    
    for play in range(0, len(playsString)):
      plays.append(int(playsString[play]))
    
    aux_node = NodeConnectFour(True,value="",state=self.initState, operators=self.operators)

    state = []
    for index in plays:
      state = aux_node.getState(index)
      aux_node.player = not aux_node.player
      aux_node.state = state
    return state

  def getPlayerFromHTML(self):
    player = str(self.js.document.getElementById('secret_pc_player').innerHTML)
    if int(player) == 1:
      return True
    else:
      return False

    return True

  def placePlayInHTML (self, play_col):
    playsString = str(self.js.document.getElementById('secret_play_list').innerHTML)
    playsString = playsString + str(play_col)
    self.js.document.getElementById('secret_play_list').innerHTML = playsString

@app.route("/")
def index():
  return App.render(render_template('index.html'))

if __name__ == '__main__':
  app.run(port=8000)