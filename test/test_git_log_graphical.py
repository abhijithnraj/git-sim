from manim import *
from manim.utils.testing.frames_comparison import frames_comparison
import os
from git_sim.log import Log, handle_animations, log
import git
import warnings
import shutil
import pytest
from temp_git_creator import TempGitCreator
from copy import deepcopy
from git_sim.settings import settings
settings.animate = True
settings.auto_open = False
settings.stdout = True


__module_test__ = "gitlog"


class TestGitLogGraphical:
    git_sim_tests_directory = os.path.join(os.path.expanduser('~'), "/tmp")

    def setup_method(self, method):
        # TODO: Should warninigs be ignored
        warnings.simplefilter("ignore")
        self.git_sim_tests_directory = os.path.join(
            TestGitLogGraphical.git_sim_tests_directory, "git_sim_"+str(method))
        if (os.path.exists(self.git_sim_tests_directory)):
            shutil.rmtree(self.git_sim_tests_directory)
        os.makedirs(self.git_sim_tests_directory)
        os.chdir(self.git_sim_tests_directory)
        self.temp_git_creator = TempGitCreator(self.git_sim_tests_directory)

    def teardown_method(self, method):
        if (os.path.exists(self.git_sim_tests_directory)):
            shutil.rmtree(self.git_sim_tests_directory)

    # FIXME: Adding last_frame=False should generate video and compare multiple frames but is currently throwing errors.
    @frames_comparison(last_frame=True)
    @pytest.mark.parametrize("test_no_commmits", [2, 3, 4, 6, 7, 9, 10, 11, 12, 13, 15, 100])
    @pytest.mark.parametrize("test_commits_to_show", [2, 3, 12, 15])
    def test_gitlog(self, scene, test_no_commmits, test_commits_to_show):
        self.temp_git_creator.run_init()
        commit_id_list = self.temp_git_creator.generate_commits(
            test_no_commmits, "Test Commit", "two_commit_file")
        log = Log(commits=test_commits_to_show)
        log.construct()
        scene.mobjects = deepcopy(log.mobjects)
        scene.renderer.camera = deepcopy(log.renderer.camera)
        scene.animations = deepcopy(log.animations)
        scene.last_t = 0
