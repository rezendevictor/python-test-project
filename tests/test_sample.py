from unittest import TestCase

from src import my_module

class MyTest(TestCase):
    def test(self):
        result = my_module.cheapest(busca="Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)")
        self.assertEqual(result, "Lakewood")
        result = my_module.cheapest(busca="Regular:20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)")
        self.assertEqual(result, "Bridgewood")
        result = my_module.cheapest(busca="Reward: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)")
        self.assertEqual(result, "Ridgewood")