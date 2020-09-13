var users = {
  "company_A": "password_A",
  "company_B": "password_B",
  "company_C": "password_C",
  "company_D": "password_D"
};

function validate() {
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;
  if ((username in users) && password == users[username]) {
    return true;
  } else {
    alert("Invalid Credentials");
    return false;
  };
};