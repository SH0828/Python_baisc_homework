import os
import sys

print(f"현재 작업 디렉토리: {os.getcwd()}")
print(f"Python 버전: {sys.version.splitlines()[0]}")
print(f"운영체제: {sys.platform}")

path_env = os.environ.get('PATH', '')
path_parts = path_env.split(os.pathsep)
if path_parts:
    print(f"환경 변수 PATH 일부: {path_parts[0]}:...")

file_path = "/Users/username/documents/report.txt"
print("파일 경로 정보:")
print(f"- 디렉토리: {os.path.dirname(file_path)}")
print(f"- 파일명: {os.path.basename(file_path)}")
print(f"- 확장자: {os.path.splitext(file_path)[1]}")

print(f"파일 존재 여부: {os.path.exists(file_path)}")