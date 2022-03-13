import world
import dataloader
import model
import utils
from pprint import pprint

if world.dataset in ['gowalla', 'yelp2018', 'amazon-book']:
    dataset = dataloader.Loader(path="../data/"+world.dataset)
elif world.dataset == 'lastfm':
    dataset = dataloader.LastFM()
elif world.dataset == 'netflix':
    dataset = dataloader.LoaderNetflix()

print('===========config================')
pprint(world.config)
print("cores for test:", world.CORES)
print("comment:", world.comment)
print("tensorboard:", world.tensorboard)
print("LOAD:", world.LOAD)
print("Weight path:", world.PATH)
print("Test Topks:", world.topks)
print("using bpr loss")
print('===========end===================')

MODELS = {
    'mf': model.PureMF,
    'lgn': model.LightGCN,
    'mod_lgn': model.mod_LightGCN
}
# MODELS = {
#     'mod_lgn': model.mod_LightGCN
# }