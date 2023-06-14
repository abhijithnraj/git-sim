import os
import git

class TempGitCreator:
    def __init__(self,git_dir_path):
        if(os.path.exists(git_dir_path)):
            self.dir = git_dir_path
        else:
            raise FileNotFoundError(f"Directory Path {git_dir_path} not found")
        try:
            self.repo = git.Repo(self.dir)
        except git.exc.InvalidGitRepositoryError as e:
            self.repo=None
            pass
    def run_init(self):
        git.Repo.init(self.dir)
        self.repo = git.Repo(self.dir)

    def create_file_and_commit(self,file_name,file_content,commit_message):
        # TODO: Assert that the file_name does not have a directory base
        if(not self.repo):
            self.repo = git.Repo(self.dir)
        complete_file_name = os.path.join(self.dir,file_name)
        with open(complete_file_name, "w") as f:
            f.write(file_content)
            f.close()
        self.repo.index.add([complete_file_name])
        author = git.Actor("An author", "author@example.com")
        committer = git.Actor("A committer", "committer@example.com")
        import datetime
        return str(self.repo.index.commit(commit_message,commit_date=datetime.date(2020, 7, 21).strftime('%Y-%m-%d %H:%M:%S'), author_date=datetime.date(2020, 7, 21).strftime('%Y-%m-%d %H:%M:%S'), author =author,committer=committer))[:6]
    
    def generate_commits(self,no_commits:int,commit_message_base:str,file_base:str):
        assert(no_commits>=1)
        commit_id_list=[]
        for i in range(no_commits):
            expected_commit_message = f"{commit_message_base}{i+1}"
            expected_commit_id = self.create_file_and_commit(f"{file_base}{i+1}","",expected_commit_message)
            commit_id_list.append(expected_commit_id)
        assert(len(commit_id_list)==no_commits)
        return commit_id_list
