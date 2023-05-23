function displayChampions(champions) {
  championList.innerHTML = '';

  champions.forEach(async (champion) => {
    const championItem = `
      <div class="champion">
        <img src="${champion.image}" alt="${champion.name}">
        <h3>${champion.name}</h3>
        <div class="top-players">
          <h4>Top players with highest mastery points:</h4>
          <div class="top-players-icons"></div>
        </div>
      </div>
    `;
    championList.innerHTML += championItem;

    const topPlayersContainer = championList.querySelector('.top-players-icons');
    const topPlayers = await getTopPlayers(champion.id);
    topPlayers.forEach((player) => {
      const playerIcon = `
        <img src="${player.image}" alt="${player.name}" title="${player.name} - ${player.points} mastery points">
      `;
      topPlayersContainer.innerHTML += playerIcon;
    });
  }); // added closing curly brace for forEach loop here
} // moved closing curly brace for displayChampions function here and closed top-players div tag
