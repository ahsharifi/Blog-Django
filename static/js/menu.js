const menuItems = document.querySelectorAll(".site-header nav a");
const path = location.pathname.split("/").slice(0, -1).join("/");

switch (path) {
  case "":
    menuItems[0].classList.add("is-active");
    break;
  case "/blogs":
    menuItems[1].classList.add("is-active");
    break;
  case "/blogs/blog-details":
    menuItems[1].classList.add("is-active");
    break;
  case "/shop":
    menuItems[2].classList.add("is-active");
    break;
  case "/shop/details":
    menuItems[2].classList.add("is-active");
    break;
  case "/about":
    menuItems[3].classList.add("is-active");
    break;
  case "/contact":
    menuItems[4].classList.add("is-active");
    break;
}
