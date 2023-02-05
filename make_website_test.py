# SHI ZHANG
# 15636078
# I WORKED ALONE WITHOUT HELP.

import unittest

from make_website import *

class MakeWebsite_Test(unittest.TestCase):

    def test_surround_block(self):
        # test text with surrounding h1 tags
        self.assertEqual("<h1>Eagles</h1>", surround_block('h1', 'Eagles'))

        # test text with surrounding h2 tags
        self.assertEqual("<h2>Red Sox</h2>", surround_block('h2', 'Red Sox'))

        # test text with surrounding p tags
        self.assertEqual('<p>Lorem ipsum dolor sit amet, consectetur ' +
                         'adipiscing elit. Sed ac felis sit amet ante porta ' +
                         'hendrerit at at urna.</p>',
                         surround_block('p', 'Lorem ipsum dolor sit amet, consectetur ' +
                                        'adipiscing elit. Sed ac felis sit amet ante porta ' +
                                        'hendrerit at at urna.'))

    def test_create_email_link(self):

        # test email with @ sign
        self.assertEqual(
            '<a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>',
            create_email_link('lbrandon@wharton.upenn.edu')
        )

        # test email with @ sign
        self.assertEqual(
            '<a href="mailto:krakowsky@outlook.com">krakowsky[aT]outlook.com</a>',
            create_email_link('krakowsky@outlook.com')
        )

        # test email without @ sign
        self.assertEqual(
            '<a href="mailto:lbrandon.at.seas.upenn.edu">lbrandon.at.seas.upenn.edu</a>',
            create_email_link('lbrandon.at.seas.upenn.edu')
        )

    def test_reading_file(self):
        # test first line in sample resume
        self.assertEqual(
            'I.M. Student', reading_file('resume.txt')[0].strip()
        )

        # test the second line in resume_courses_weird_punc
        self.assertEqual(
            'Courses:-_##$&^!*()Programming Languages and Techniques, Biomedical image analysis, Software Engineering', reading_file('TestResumes/resume_courses_weird_punc/resume.txt')[1].strip()
        )

    def test_detecting_name(self):
        # test sample resume
        self.assertEqual(
            'I.M. Student', detecting_name('resume.txt')
        )

        # test bad name lowercase
        self.assertEqual(
            'Invalid Name', detecting_name('TestResumes/resume_bad_name_lowercase/resume.txt')
        )

    def test_detecting_email(self):
        # test email with whitespace
        self.assertEqual(
            'lbrandon@wharton.upenn.edu', detecting_email('TestResumes/resume_template_email_w_whitespace/resume.txt')
        )

        # test wrong email
        self.assertEqual(
            '',  detecting_email('TestResumes/resume_wrong_email/resume.txt')
        )

    def test_detecting_course(self):
        # test course with whitespace
        self.assertEqual(
            ['Programming Languages and Techniques', 'Biomedical image analysis', 'Pottery'], detecting_course('TestResumes/resume_courses_w_whitespace/resume.txt')
        )

        # test course with weird punctuation
        self.assertEqual(
            ['Programming Languages and Techniques', 'Biomedical image analysis', 'Software Engineering'], detecting_course('TestResumes/resume_courses_weird_punc/resume.txt')
        )

    def test_detecting_project(self):
        # test project with whitespace
        self.assertEqual(
            'Biomedical Imaging - Developed a semi-automatic image mosaic program based on SIFT algorithm (using Matlab)', detecting_project('TestResumes/resume_projects_w_whitespace/resume.txt')[1]
        )

        # test project with blank lines
        self.assertEqual(
            'Biomedical Imaging - Developed a semi-automatic image mosaic program based on SIFT algorithm (using Matlab)', detecting_project('TestResumes/resume_projects_with_blanks/resume.txt')[1]
        )


if __name__ == '__main__':
    unittest.main()
