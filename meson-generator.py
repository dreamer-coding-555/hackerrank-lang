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
    name = solution.get_basename()[3:-4]
    executable(f'prog-{solution.get_basename()[0:2] if len(solutions) >= 10 else solution.get_basename()[0]}', solution)
endforeach
        """
        with open(os.path.join(solutions_dir, 'meson.build'), 'w') as file:
            file.write(subdirectory_script)

if __name__ == "__main__":
    meson_generator = MesonScriptGenerator(project_name='Hacker Rank')
    meson_generator.generate_source_build_script()
    meson_generator.generate_subdirectory_build_script()
