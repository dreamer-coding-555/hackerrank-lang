import os

class MesonScriptGenerator:
    def __init__(self, project_name='YourProject'):
        self.project_name = project_name

    def generate_source_build_script(self):
        source_script = f"""
project('{self.project_name}', 'cpp')

subdir('solutions')
        """
        with open('meson.build', 'w') as file:
            file.write(source_script)

    def generate_subdirectory_build_script(self):
        solutions_dir = 'solutions'
        solutions = [f for f in os.listdir(solutions_dir) if f.endswith('.cpp')]

        subdirectory_script = f"""
solutions = {len(solutions)}

foreach solution : solutions
    index_str = (solution[0:2] if len(solutions) >= 10 else solution[0]) # Correct slicing syntax
    name = solution[3:-4]  # Remove index and extension
    executable('prog-' + index_str, solution)
endforeach
        """
        with open(os.path.join(solutions_dir, 'meson.build'), 'w') as file:
            file.write(subdirectory_script)

if __name__ == "__main__":
    meson_generator = MesonScriptGenerator(project_name='Hacker Rank')
    meson_generator.generate_source_build_script()
    meson_generator.generate_subdirectory_build_script()
