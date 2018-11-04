"""
A script to test how the github download from a remote github.com repo to a 
users home directory

"""
import os
import git
import shutil
from git import Repo
from pwd import getpwnam

ERASE_DIR = True

def create_dir_hook(username):
    # username = spawner.user.name
    username = "fist.last"
    print(f'User Name: {username}')
    uid = getpwnam(username).pw_uid
    print(f'{username} user numerical user id uid = {uid}')
    gid = getpwnam(username).pw_gid
    print(f'{username} user numerical group id gid = {gid}')
    DIR_NAME = os.path.join("/home", username)
    git_url = "https://github.com/ProfessorKazarinoff/ENGR101.git"
    repo_dir = os.path.join(DIR_NAME, 'notebooks')
    print(f'Notebooks will be cloned from github to the {repo_dir} directory')

    if ERASE_DIR==True:
        if os.path.isdir(repo_dir):
            print(f'existing {repo_dir} found')
            shutil.rmtree(repo_dir)
            print(f'existing {repo_dir} removed')
        os.mkdir(repo_dir)
        print(f'new emtpy {repo_dir} created')
        clone_repo(username, git_url,repo_dir)

    if ERASE_DIR==False and not(os.path.isdir(repo_dir)):
        os.mkdir(repo_dir)
        print(f'new emtpy {repo_dir} created')
        clone_repo(username, git_url, repo_dir)

    if ERASE_DIR==False and os.path.isdir(repo_dir):
        pass

    # for file in os.listdir(DIR_NAME):
    #    if os.path.isfile(os.path.join(DIR_NAME,file)):
    #        os.remove(os.path.join(DIR_NAME,file))
    # REMOTE_URL = "https://github.com/ProfessorKazarinoff/ENGR101.git"
    # if os.path.isdir(os.path.join(DIR_NAME,"notebooks")):
    #    shutil.rmtree(os.path.join(DIR_NAME,"notebooks"))
    # if os.path.isdir(os.path.join(DIR_NAME, "notes")):
    #    shutil.rmtree(os.path.join(DIR_NAME, "notes"))
    # os.chdir(DIR_NAME)

def clone_repo(user,
               git_url = "https://github.com/ProfessorKazarinoff/ENGR101.git",
               repo_dir = 'notebooks'):
        Repo.clone_from(git_url, repo_dir)
        print(f'User Name: {user}')
        uid = getpwnam(user).pw_uid
        print(f'{user} user numerical user id uid = {uid}')
        gid = getpwnam(user).pw_gid
        print(f'{user} user numerical group id gid = {gid}')
        print(f'Repo from {git_url} cloned into {repo_dir}')
        print(f'changing permissions of dirs and files in {repo_dir}')
        for root, dirs, files in os.walk(repo_dir):
            for d in dirs:
                print(f'found directory {d}')
                shutil.chown(os.path.join(root, d), user=uid, group=gid)
                print(f'changed permissions of {d} to uid ={uid} and gid = {gid}')
            for f in files:
                print(f'found file {f}')
                shutil.chown(os.path.join(root, f), user=uid, group=gid)
                print(f'changed permissions of {f} to uid = {uid} and gid = {gid}')


def main():
    create_dir_hook('fist.last')


if __name__ == "__main__":
    main()
