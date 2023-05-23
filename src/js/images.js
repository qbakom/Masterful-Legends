API_KEY = 'RGAPI-1f2a2cf5-6667-4ccb-adff-6570d9db43c6'

async function getTopPlayers(championId) {
    const response = await fetch(`https://lolpros.gg/api/champion/${championId}/top`);
    const topPlayers = await response.json();
    return topPlayers.slice(0, 20);
  }
  
  async function getProfileIcon(summonerId) {
    const response = await fetch(`https://euw1.api.riotgames.com/lol/summoner/v4/summoners/${summonerId}?api_key=${API_KEY}`);
    const summonerData = await response.json();
    return `http://ddragon.leagueoflegends.com/cdn/11.6.1/img/profileicon/${summonerData.profileIconId}.png`;
  }
  
  async function displayTopPlayers(championId, topPlayersContainer) {
    const topPlayers = await getTopPlayers(championId);
    
    topPlayers.forEach(async (player) => {
      const profileIcon = await getProfileIcon(player.summonerId);
      const profileIconElement = `
        <img src="${profileIcon}" alt="${player.summonerName}">
      `;
      topPlayersContainer.innerHTML += profileIconElement;
    });
  }