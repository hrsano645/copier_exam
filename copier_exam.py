import copier

data = {"project_number": "SND0003", "project_date": "2023-12-21"}
copier.run_copy("./my_template", "./generated_project3", data)
