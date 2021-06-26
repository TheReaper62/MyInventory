import pyrebase,time

config = {
  "apiKey": "AIzaSyDcrQplIY9zL2-q-5t3SPjaCtY0kjKlvow",
  "authDomain": "embededinventory.firebaseapp.com",
  "databaseURL": "https://embededinventory-default-rtdb.us-central1.firebasedatabase.app",
  "storageBucket": "embededinventory.appspot.com",
  "serviceAccount": "embededinventory.json"
}
start = time.time()
print("Connecting to Firebase...")
firebase = pyrebase.initialize_app(config)
firebase = firebase.database()
print(f"Successfully Connected to Firebase in {time.time()-start} seconds.")

def jus_return(key=None):
    if key==None:
        return firebase.val()
    else:
        print(firebase.child(key).get())
        return firebase.child(key).get()

def remove_key(depth,*path):
    if depth==2:
        firebase.child(path[0]).child(path[1]).remove()
        print("Removed>>>",path)
    else:
        raise InterruptedError

jus_return("administrators")