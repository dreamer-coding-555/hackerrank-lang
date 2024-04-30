import os

class CMakeScriptGenerator:
    def __init__(self, project_name='YourProject'):
        self.project_name = project_name

    def generate_root_cmake_file(self):
        root_script = f"""
cmake_minimum_required(VERSION 3.10)
project({self.project_name} LANGUAGES CXX)

add_subdirectory(solutions)
"""
        with open('CMakeLists.txt', 'w') as file:
            file.write(root_script)

    def generate_subdirectory_cmake_files(self):
        solutions_dir = 'solutions'
        solutions = [os.path.splitext(f)[0] for f in os.listdir(solutions_dir) if f.endswith('.cpp')]
        solved = len(solutions)
    
        subdirectory_script = f"""
set(solutions {";\n    ".join(solutions)})

foreach(solution ${{solutions}})
    add_executable(${{solution}} ${{solution}}.cpp)
endforeach()
"""
        os.makedirs(solutions_dir, exist_ok=True)
        with open(os.path.join(solutions_dir, 'CMakeLists.txt'), 'w') as file:
            file.write(subdirectory_script)


if __name__ == "__main__":
    cmake_generator = CMakeScriptGenerator(project_name='Hacker Rank')
    cmake_generator.generate_root_cmake_file()
    cmake_generator.generate_subdirectory_cmake_files()
