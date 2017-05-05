import sys
sys.path.append('../config')
from config.Config import Config
from subprocess import Popen
from subprocess import PIPE

class HandBrakeAdapter:

    @staticmethod
    def run(inputFile, outputFile):
        command = HandBrakeAdapter.__buildCommand(inputFile, outputFile)
        p = Popen(command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()
        if p.returncode != 0:
            raise Exception(stderr)

    @staticmethod
    def __buildCommand(inputFile, outputFile):
        command = []
        command.append('HandBrakeCLI')
        command.append('-i')
        command.append(inputFile)
        command.append('-o')
        command.append(outputFile)
        command.append('-x')
        command.append(Config.get('handbrake.profile'))
        return command
