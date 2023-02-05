# SHI ZHANG
# 15636078
# I WORKED ALONE WITHOUT HELP.

def reading_file(txt_input_file):
    """reads the file and stores it in memory as a list of lines"""
    with open(txt_input_file) as f:
        lst = f.readlines()
    return lst

def detecting_name(txt_input_file):
    """detecting the name by extracting the first line
    remove the leading or trailing white space"""
    name = reading_file(txt_input_file)[0].strip().split(' ')
    # Verify the first letter in surname and given name are both uppercase
    if name[0][0].isupper():
        name_string = " ".join(name)
        return name_string
    else:
        return 'Invalid Name'

def detecting_email(txt_input_file):
    """detect and verify the email address, return the valid email address"""
    for line in reading_file(txt_input_file):
        line = line.strip()
        find_index1 = line.find('@')
        find_index2 = line.find('[aT]')
        # situation 1: the email contains '@'
        if find_index1 != -1 and find_index2 == -1:
            # verify no digit or numbers in email
            if any(i.isdigit() for i in line):
                return ""
            # verify the last 4 digits in email
            else:
                if (line[-4:] == '.com' or line[-4:] == '.edu') and line[find_index1+1].islower() == True:
                    return line
                else:
                    return ""

        # situation 2: the email contains '[aT]'
        if find_index1 == -1 and find_index2 != -1:
            # verify no digit or numbers in email
            if any(i.isdigit() for i in line):
                return ""
            # verify the last 4 digits in email
            else:
                if (line[-4:] == '.com' or line[-4:] == '.edu') and line[find_index1 + 4].islower() == True:
                    return line
                else:
                    return ""



def detecting_course(txt_input_file):
    """Looking for word 'Courses' from lines in the file and return a list of courses"""
    courses = []
    for line in reading_file(txt_input_file):
        if 'Courses' in line:
            course_line = line
    # remove leading or trailing whitespace
    course_line.strip()
    # determine the first range by finding the punctuation
    range_1 = course_line.index(':')
    # remove the part of string before ':', including ':'
    line_trim1 = course_line[range_1+1:]
    # determine the second range of actual course in string
    for i in line_trim1:
        # verify the first alphabetic letter index
        if i.isalpha():
            range_2 = line_trim1.index(i)
            break
    line_trim2 = line_trim1[range_2:].strip().split(',')
    # remove any leading or trailing whitespace for each item in list
    for course in line_trim2:
        course = course.strip()
        courses.append(course)
    return courses

def detecting_project(txt_input_file):
    """looking for word ’projects' from lines in the file and return a list of projects"""
    projects = []
    # find the list item index define the start and end of projects
    lines = reading_file(txt_input_file)
    for line in lines:
        line.strip()
        if '----------' in line:
            end_index = lines.index(line)
        if 'Projects' in line:
            start_index = lines.index(line)

    # get the list that only has projects and remove the whitespace, store it in the projects list
    project_content = lines[start_index+1:end_index]
    for project in project_content:
        project = project.strip()
        if len(project.split()) != 0:
            projects.append(project)

    return projects



def surround_block(tag, text):
    """
    Surrounds the given text with the given html tag and returns the string.
    """
    html_string = '<'+str(tag)+'>'+str(text)+'</'+str(tag)+'>'
    return html_string

def create_email_link(email_address):
    """
    Creates an email link with the given email_address.
    To cut down on spammers harvesting the email address from the webpage,
    displays the email address with [aT] instead of @.

    Example: Given the email address: lbrandon@wharton.upenn.edu
    Generates the email link: <a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>

    Note: If, for some reason the email address does not contain @,
    use the email address as is and don't replace anything.
    """
    if '@' in email_address:
        email_link = '<a href="mailto:'+str(email_address)+'">'+str(email_address).replace('@', '[aT]')+'</a>'
        return email_link
    else:
        email_link = '<a href="mailto:' + str(email_address) + '">' + str(email_address) + '</a>'
        return email_link

def generate_html(txt_input_file, html_output_file):
    """
    Loads given txt_input_file,
    gets the name, email address, list of projects, and list of courses,
    then writes the info to the given html_output_file.

    # Hint(s):
    # call function(s) to load given txt_input_file
    # call function(s) to get name
    # call function(s) to get email address
    # call function(s) to get list of projects
    # call function(s) to get list of courses
    # call function(s) to write the name, email address, list of projects, and list of courses to the given html_output_file
    """

    # get information from given text file
    name = detecting_name(txt_input_file)
    # print("name: ", name)
    email_address = detecting_email(txt_input_file)
    # print("email: ", email_address)
    projects = detecting_project(txt_input_file)
    # print("projects: ", projects)
    courses = detecting_course(txt_input_file)
    # print("courses: ", courses)

    # the first line is to create the initial tag to make sure all the text is enclosed within tags
    line_1 = "<div id=\"page-wrap\">"

    # write the basic information from the extracted information in the text file
    name_line = surround_block('h1', name)
    email_line = surround_block('p', 'Email:' + create_email_link(email_address))
    basic_info = surround_block('div', name_line + email_line)

    # write the project section from the extracted information in the text file
    project_line1 = surround_block('h2', 'Projects')
    project_bullet_list = []
    for project in projects:
        if len(project) != 0:
            project_line = surround_block('li', project)
            project_bullet_list.append(project_line)
        else:
            continue
    project_bullet_string = ''.join(project_bullet_list)
    project_bullet_string = surround_block('ul', project_bullet_string)
    project_section = surround_block('div', project_line1 + project_bullet_string)

    # write the course section from the extracted information in the text file
    course_line1 = surround_block('h3', 'Courses')
    course_string = surround_block('span', ', '.join(courses))
    course_section = surround_block('div', course_line1 + course_string)

    # close the html tags
    close_section = '</div>'+'\n'+'</body>'+'\n'+'</html>'

    # compile all the information back to a list:
    write_content = [line_1, basic_info, project_section, course_section, close_section]

    # write all the information gathered to html file:
    with open(html_output_file, 'w') as my_file:
        for content in write_content:
            my_file.write(content)

    # close the html file
    my_file.close()


def main():

    # DO NOT REMOVE OR UPDATE THIS CODE
    # generate resume.html file from provided sample resume.txt
    generate_html('resume.txt', 'resume.html')

    # DO NOT REMOVE OR UPDATE THIS CODE.
    # Uncomment each call to the generate_html function when you’re ready
    # to test how your program handles each additional test resume.txt file

    generate_html('TestResumes/resume_bad_name_lowercase/resume.txt', 'TestResumes/resume_bad_name_lowercase/resume.html')
    generate_html('TestResumes/resume_courses_w_whitespace/resume.txt', 'TestResumes/resume_courses_w_whitespace/resume.html')
    generate_html('TestResumes/resume_courses_weird_punc/resume.txt', 'TestResumes/resume_courses_weird_punc/resume.html')
    generate_html('TestResumes/resume_projects_w_whitespace/resume.txt', 'TestResumes/resume_projects_w_whitespace/resume.html')
    generate_html('TestResumes/resume_projects_with_blanks/resume.txt', 'TestResumes/resume_projects_with_blanks/resume.html')
    generate_html('TestResumes/resume_template_email_w_whitespace/resume.txt', 'TestResumes/resume_template_email_w_whitespace/resume.html')
    generate_html('TestResumes/resume_wrong_email/resume.txt', 'TestResumes/resume_wrong_email/resume.html')


    # If you want to test additional resume files, call the generate_html function with the given .txt file
    # and desired name of output .html file

if __name__ == '__main__':
    main()