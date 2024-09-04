function getFormattedResult(data) {
  let totalCredit = 0;
  
  // Calculate total credit
  data.forEach(course => {
    totalCredit += course.totalCredit;
  });

  // Start building the message
  let message = `
**Result for ${data[0].semesterName} ${data[0].semesterYear} (Semester ID: ${data[0].semesterId})**\n
**Student ID:** ${data[0].studentId}

\`| Course Code | Course Title                      | Credit | Grade | Point |
|-------------|-----------------------------------|--------|-------|-------|\`
`;

  // Add each course to the message
  data.forEach(course => {
    message += `| \`${course.customCourseId}\` | ${course.courseTitle} | ${course.totalCredit} | ${course.gradeLetter} | ${course.pointEquivalent} |\n`;
  });

  // Final message with CGPA and total credit
  message += `
**CGPA:** \`${data[0].cgpa}\`
**Total Credit:** \`${totalCredit}\`

**_Note: \`I\` indicates Incomplete grade._**
`;

  return message;
}

module.exports = getFormattedResult;
