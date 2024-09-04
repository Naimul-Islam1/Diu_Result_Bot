const axios = require('axios');

async function getResult(semester_id, student_id) {
  const url = `http://203.190.10.22:8189/result?grecaptcha&semesterId=${semester_id}&studentId=${student_id}`;

  try {
    const response = await axios.get(url);
    if (response.status === 200) {
      return response.data;
    } else {
      return null;
    }
  } catch (error) {
    console.error('Error fetching the result:', error);
    return null;
  }
}

module.exports = getResult;
