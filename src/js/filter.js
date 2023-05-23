const searchBar = document.getElementById('search-bar');
const championList = document.getElementById('champion-list');

searchBar.addEventListener('keyup', (e) => {
  const searchString = e.target.value.toLowerCase();
  
  const filteredChampions = champions.filter(champion => {
    return champion.name.toLowerCase().includes(searchString);
  });
  
  displayChampions(filteredChampions);
});

function displayChampions(champions) {
  championList.innerHTML = '';
  
  champions.forEach(champion => {
    const championItem = `
      <div class="champion">
        <img src="${champion.image}" alt="${champion.name}">
        <h3>${champion.name}</h3>
        <div class="top-players">
          <!-- Add code to display images of top players with highest mastery points -->
        </div>
      </div>
    `;
    championList.innerHTML += championItem;
  });
}
