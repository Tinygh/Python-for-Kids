import pickle
favorite_things = {'mom' : 'apple','dad' : 'orange','baby' : ['ice cream','candy','grapes'],'aaa':123}
save_file = open('/work/pj/favorites.bat','wb')
print('save_file:',save_file)
pickle.dump(favorite_things,save_file)
save_file.close
load_file = open('/work/pj/favorites.bat','rb')
loaded_favorite_things = pickle.load(load_file)
print('load_file:',load_file)
load_file.close
