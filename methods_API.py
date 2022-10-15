import requests
class SuperHero:
    def get_stats(self, url):
        hero_stats = self.get_json(url)
        return hero_stats
    
    def get_json(self, url):
        response = requests.get(url)
        return response.json()
    
def Max_intelligence():
    all_stats = {'Hulk': Hulk(), 'Captain_America': Captain_America(), 'Thanos': Thanos()}
    return max(all_stats)

def Hulk():
    Hulk = SuperHero()
    Hulk_stats=Hulk.get_stats(url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/powerstats/332.json')
    return Hulk_stats['intelligence']

def Captain_America():
    Captain_America = SuperHero()
    Captain_America_stats=Captain_America.get_stats(url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/powerstats/149.json')
    return Captain_America_stats['intelligence']

def Thanos():
    Thanos = SuperHero()
    Thanos_stats=Thanos.get_stats(url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/powerstats/655.json')
    return Thanos_stats['intelligence']

