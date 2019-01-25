# sshClient
User-friendly software to connect to host via ssh

How to use:

	At first, install required libs:
	pip3 install --user paramiko && pip3 install --user scp (Linux/macOS)
	pip-install --upgrade paramiko(windows)
	pip-install --upgrade scp(windows)

	startServer.py works if cannot ping host.

	config.conf contains hostname, port, username and password of host

	constants.py the same, used for connect to host in main.py, startServer.py

	hostCheck.py should work everytime to check host is working or not

	main.py used for working with host(copying and deleting files, other actions restricted, because it may cause problems with remote server)
	if user will try to use rm -rf, soft will stop instantly.
