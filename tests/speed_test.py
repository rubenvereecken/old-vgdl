'''
Created on Oct 8, 2013

@author: tom.schaul
'''


def testInteractions():
    from pybrain.rl.experiments.episodic import EpisodicExperiment
    from vgdl.core import VGDLParser
    from examples.gridphysics.aliens import aliens_level,aliens_game
    #from examples.gridphysics.sokoban import so
    from pybrain.rl.agents.agent import Agent
    from vgdl.interfaces import GameEnvironment, GameTask
    
    class DummyAgent(Agent):
        total = 4
        def getAction(self):
            #res = randint(0, self.total - 1)
            return 1
        
    map_str, game_str = aliens_level,aliens_game
    g = VGDLParser().parseGame(game_str)
    g.buildLevel(map_str)
    
    env = GameEnvironment(g, visualize=False, actionDelay=0)
    task = GameTask(env)
    agent = DummyAgent()
    exper = EpisodicExperiment(task, agent)
    res = exper.doEpisodes(2)
    print res
     
def testLoadSave():
    from vgdl.core import VGDLParser
    from examples.gridphysics.aliens import aliens_level,aliens_game
        
    map_str, game_str = aliens_level,aliens_game
    g = VGDLParser().parseGame(game_str)
    g.buildLevel(map_str)
    
    for _ in range(1000):
        s = g.getFullState()
        g.setFullState(s)
    
if __name__ == "__main__":
    from pybrain.tests.helpers import sortedProfiling
    sortedProfiling('testInteractions()')
    #sortedProfiling('testLoadSave()')