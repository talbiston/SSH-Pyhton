#!/usr/bin/python2

import paramiko
from time import sleep
import argparse
from paramikoe import SSHClientInteraction
from sys import argv


def py_ssh(ip_add, u_name, p_word, com):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip_add, username=u_name, password=p_word)
    interact = SSHClientInteraction(ssh, timeout=10, display=True)

    for i in com:
        interact.send(com)
        interact.expect('*:~$')
        conData = interact.current_output_clean
        return conData


def Main():

    parser = argparse.ArgumentParser()
    parser.add_argument('ip_or_host', help='Enter ip or Hostname', type=str)
    parser.add_argument('username', help='Enter Username', type=str)
    parser.add_argument('password', help='Enter Password', type=str)

    group1 = parser.add_mutually_exclusive_group()

    group1.add_argument('-c', '--command', help='Enter a command to run')
    group1.add_argument('-s', '--script', help='Read commands from file')
    parser.add_argument('-o', '--output', help="output to file")
    in_flag = parser.parse_args()

    if in_flag.command:
        commands = in_flag.command

        if in_flag.output:
            consol = py_ssh(in_flag.ip_or_host, in_flag.username, in_flag.password, commands)
            out_file = open(in_flag.output, 'w')
            out_file.write(consol)
            out_file.close()
            print "Save in file " + in_flag.output
        else:
            consol = py_ssh(in_flag.ip_or_host, in_flag.username, in_flag.password, commands)
            print consol

    if in_flag.script:
        script_Data = open(in_flag.script, 'r')
        commands = script_Data.readlines()

        if in_flag.output:
            consol = py_ssh(in_flag.ip_or_host, in_flag.username, in_flag.password, commands)
            out_file = open(in_flag.output, 'w')
            out_file.write(consol)
            out_file.close()
            print "Save in file " + in_flag.output
        else:
            consol = py_ssh(in_flag.ip_or_host, in_flag.username, in_flag.password, commands)
            print consol

        script_Data.close()

if __name__ == "__main__":
    Main()



__author__ = 'todd'
