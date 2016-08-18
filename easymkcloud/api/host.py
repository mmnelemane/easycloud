# Host Management and Preparation Interface

from manager import Manager

class HostManager(Manager):
    # This class provides management APIs to handle host node setup,
    # allocation, and preparation of host with the prerequisites for
    # for deploying the cloud. The tasks involve updating the repos
    # managing the licences and certificates, allocating roles and
    # installing the required packages.
    def __init__(self):
        pass

    def create(self):
        pass

    def destroy(self):
        pass

    def update(self):
        pass

    def list(self):
        pass

    def repo_update(self):
        # Add and update all necessary repositories
        pass

    def install(self):
        # Install and update all necessary packages
        pass

