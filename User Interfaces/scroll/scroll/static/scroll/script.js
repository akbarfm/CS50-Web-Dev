// Start with first post
let counter = 1;

// Load posts 20 at a time
const quantity = 20;

// When DOM loads, render the first 20 posts
document.addEventListener('DOMContentLoaded', load);

// // If scrolled to bottom, load the next 20 posts
// window.onscroll = () => {
//     if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
//         load();
//     }
// };
// ------------------------------------------------------------------
// An upgrade from the previous function. This function add a one second delay after running load() so that it will only update 20 numbers.
// The previous function sometimes add 100+ number. Probably because the load() function run multiple times when.
let canRun = true;
window.onscroll = () => {
    if (canRun && window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        canRun = false;
        setTimeout(() => {
            load();
            canRun = true;
        }, 1000);
    }
};

function load() {
    const start = counter;
    const end = start + quantity -1;
    counter = end + 1;

    fetch(`/posts?start=${start}&end=${end}`)
    .then(response => response.json())
    .then(data=> {
        data.posts.forEach(add_post);
    })
};

function add_post(contents) {

    const post = document.createElement('div');
    post.className = 'post';
    post.innerHTML = contents;

    document.querySelector('#posts').append(post);
};