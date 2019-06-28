import argparse
import shutil
import os
import subprocess


def parse_input_args():
	parser = argparse.ArgumentParser(
		description='Python backup script')
	parser.add_argument(
		'-s',
		'--source',
		dest='source',
		nargs=1,
		required=True,
		help='Backup source path',
		type=str
		)
	parser.add_argument(
		'-t',
		'--target',
		dest='target',
		nargs=1,
		required=True,
		help='Backup target path',
		type=str
		)
	return parser.parse_args()


def backup_files():
	count_new = 0
	count_changed = 0
	count_not_changed = 0
	for path, dirs, files in os.walk(source_path):
		for directory in dirs:
			directory = target_path + path + '/' + directory
			if not os.path.isdir(directory):
				os.makedirs(directory)
		for source in files:
			source = path + '/' + source
			target = target_path + source
			try:
				if os.stat(source).st_mtime_ns > os.stat(target).st_mtime_ns:
					os.remove(target)
					shutil.copy2(source, target)
					count_changed += 1
					print('File ' + target + ' was replaced with newer version')
				elif os.stat(source).st_mtime_ns <= os.stat(target).st_mtime_ns:
					count_not_changed += 1
					continue
			except FileNotFoundError:
				shutil.copy2(source, target)
				count_new += 1
	print('Number of new files: {0}'.format(count_new))
	print('Number of changed files: {0}'.format(count_changed))
	print('Number of files that did not change: {0}'.format(count_not_changed))
	return


if __name__ == '__main__':
	input_args = parse_input_args()
	source_path = input_args.source[0]
	target_path = input_args.target[0]
	backup_files()
		
