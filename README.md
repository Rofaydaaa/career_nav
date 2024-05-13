## Careers Navigator

### DataSet Processed
- Found it in this [drive](https://drive.google.com/drive/folders/10T5x6bjPKDcJ59K8WK0QLLl12aGsqWun?usp=sharing)
- Fields after preprocessing:
```
0. "id"
1. "sourceCC"
2. "source"
3. "locale"
4. "position_name"
5. "position_workType"
6. "position_careerLevel"
7. "position_department"
8. "orgAddress_addressLine"
9. "orgAddress_level"
10. "orgAddress_country"
11. "orgAddress_state"
12. "orgAddress_city"
13. "orgCompany_nameOrg"
14. "orgCompany_homepage"
15. "url"
16. "orgTags_CATEGORIES"
17. "orgTags_REQUIREMENTS"
18. "orgTags_SKILLS"
19. "salary_text"
20. "salary"
21. "years_or_months_experience"
```
### Map_Reduce
- If you want to run map-reduce on a new data rather than the available one, you'll need to change it to txt file first with function in csv_to_txt.py file then use this txt file to run map reduce on it
- To run it, write this command: ```python <map_reduce_filename.py> <input_filename.txt>```
