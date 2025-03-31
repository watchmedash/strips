let config;
fetch('data.json')
  .then(response => response.json())
  .then(data => {
    config = data;
    initGame();
  })
  .catch(error => {
    console.error("Error loading configuration:", error);
  });

function initGame() {
  let credits;
  const savedCredits = localStorage.getItem('credits');
  if (savedCredits !== null) {
    credits = parseInt(savedCredits, 10);
  } else {
    credits = config.initialCredits;
    localStorage.setItem('credits', credits);
  }

  let userID = localStorage.getItem('userID');
  if (!userID) {
    userID = Math.floor(100000 + Math.random() * 900000).toString();
    localStorage.setItem('userID', userID);
  }

  const creditsDiv = document.getElementById('credits');
  const messageDiv = document.getElementById('message');
  const spinButton = document.getElementById('spin');
  const betInput = document.getElementById('bet');
  const withdrawButton = document.getElementById('withdraw');
  const reel1Inner = document.querySelector('#reel1 .reel-inner');
  const reel2Inner = document.querySelector('#reel2 .reel-inner');
  const reel3Inner = document.querySelector('#reel3 .reel-inner');
  const svgOverlay = document.getElementById('winning-lines');
  const resetButton = document.getElementById('resetButton'); // Reset button reference

  const updateCreditsDisplay = () => {
    const dollars = credits / 25000;
    creditsDiv.textContent = `Credits: ${credits} = $${dollars.toFixed(2)}`;
    localStorage.setItem('credits', credits);

    if (credits < 500) {  // Check if credits are under 500
      resetButton.style.display = 'inline-block';  // Show reset button when credits are under 500
    } else {
      resetButton.style.display = 'none';  // Hide reset button otherwise
    }
  };
  updateCreditsDisplay();

  const getRandomSymbol = () => {
    const totalWeight = config.symbols.reduce((sum, symbol) => sum + symbol.weight, 0);
    const randomValue = Math.random() * totalWeight;
    let currentWeight = 0;
    for (const symbol of config.symbols) {
      currentWeight += symbol.weight;
      if (randomValue <= currentWeight) {
        return symbol;
      }
    }
    return config.symbols[config.symbols.length - 1];
  };

  const winningLines = [
    [[0, 0], [0, 1], [0, 2]],
    [[1, 0], [1, 1], [1, 2]],
    [[2, 0], [2, 1], [2, 2]],
    [[0, 0], [1, 1], [2, 2]],
    [[0, 2], [1, 1], [2, 0]]
  ];

  const generateFinalGrid = () => {
    const grid = [];
    for (let r = 0; r < 3; r++) {
      grid[r] = [];
      for (let c = 0; c < 3; c++) {
        grid[r][c] = getRandomSymbol();
      }
    }
    const rForce = Math.random();
    if (rForce < 0.05) {
      const payline = winningLines[Math.floor(Math.random() * winningLines.length)];
      const forcedSymbol = getRandomSymbol();
      for (const [row, col] of payline) {
        grid[row][col] = forcedSymbol;
      }
    } else if (rForce < 0.15) {
      const payline = winningLines[Math.floor(Math.random() * winningLines.length)];
      const indices = [0, 1, 2].sort(() => Math.random() - 0.5);
      const forcedSymbol = getRandomSymbol();
      grid[payline[indices[0]][0]][payline[indices[0]][1]] = forcedSymbol;
      grid[payline[indices[1]][0]][payline[indices[1]][1]] = forcedSymbol;
      let otherSymbol;
      do {
        otherSymbol = getRandomSymbol();
      } while (otherSymbol.symbol === forcedSymbol.symbol);
      grid[payline[indices[2]][0]][payline[indices[2]][1]] = otherSymbol;
    }
    return grid;
  };

  const evaluateGrid = (grid, bet) => {
    let totalReward = 0;
    const winningLinePositions = [];

    winningLines.forEach(line => {
        const lineSymbols = line.map(([r, c]) => grid[r][c]);
        const counts = {};

        // Count occurrences of each symbol in the line
        lineSymbols.forEach(symObj => {
            counts[symObj.symbol] = (counts[symObj.symbol] || 0) + 1;
        });

        for (const sym in counts) {
            if (counts[sym] === 3) {  // Only reward for 3 of a kind
                const symbolObj = config.symbols.find(s => s.symbol === sym);
                const reward = bet * symbolObj.multiplier * 3;
                totalReward += reward;
                winningLinePositions.push(line);
                break; // Stop checking this line after a 3-match win
            }
        }
    });

    return { totalReward, winningLinePositions };
};


  const drawWinningLines = (lines) => {
    svgOverlay.innerHTML = "";
    const colCenters = [80, 160, 240];
    const rowCenters = [35, 105, 175];
    lines.forEach(line => {
      const points = line.map(([r, c]) => `${colCenters[c]},${rowCenters[r]}`).join(" ");
      const polyline = document.createElementNS("http://www.w3.org/2000/svg", "polyline");
      polyline.setAttribute("points", points);
      polyline.setAttribute("stroke", "yellow");
      polyline.setAttribute("stroke-width", "4");
      polyline.setAttribute("fill", "none");
      polyline.setAttribute("stroke-linecap", "round");
      polyline.classList.add("blinking-line");
      svgOverlay.appendChild(polyline);
    });
  };

  const animateReelDown = (reelInner, finalSymbols, duration, callback) => {
    const cellHeight = 70;
    const reelContainerHeight = 210;
    const spinCount = 150;
    let randomContent = "";
    for (let i = 0; i < spinCount; i++) {
      const randomSym = getRandomSymbol().symbol;
      randomContent += `<div class="cell">${randomSym}</div>`;
    }
    let newContent = "";
    finalSymbols.forEach(symObj => {
      newContent += `<div class="cell">${symObj.symbol}</div>`;
    });
    newContent += randomContent;
    reelInner.innerHTML = newContent;
    const totalCells = finalSymbols.length + spinCount;
    const totalHeight = totalCells * cellHeight;
    const initialTranslateY = totalHeight - reelContainerHeight;
    reelInner.style.transform = `translateY(-${initialTranslateY}px)`;
    void reelInner.offsetHeight;
    reelInner.style.transition = `transform ${duration}s cubic-bezier(0.33, 1, 0.68, 1)`;
    reelInner.style.transform = `translateY(0)`;
    reelInner.addEventListener('transitionend', function handler() {
      let finalHTML = "";
      finalSymbols.forEach(symObj => {
        finalHTML += `<div class="cell">${symObj.symbol}</div>`;
      });
      reelInner.innerHTML = finalHTML;
      reelInner.style.transition = '';
      reelInner.style.transform = 'none';
      reelInner.removeEventListener('transitionend', handler);
      callback();
    }, { once: true });
  };

  const spin = () => {
    const bet = parseInt(betInput.value) || 10;
    if (credits < bet) {
      messageDiv.textContent = "Not enough credits!";
      return;
    }
    svgOverlay.innerHTML = "";
    credits -= bet;
    updateCreditsDisplay();
    messageDiv.textContent = "";
    spinButton.disabled = true;
    const finalGrid = generateFinalGrid();
    console.table(finalGrid.map(row => row.map(cell => cell.symbol)));
    let finishedReels = 0;
    const reelFinished = () => {
      finishedReels++;
      if (finishedReels === 3) {
        const result = evaluateGrid(finalGrid, bet);
        if (result.totalReward > 0) {
          drawWinningLines(result.winningLinePositions);
          messageDiv.textContent = `Total win: +${result.totalReward} credits!`;
        } else {
          messageDiv.textContent = "No win, try again!";
        }
        credits += result.totalReward;
        updateCreditsDisplay();
        spinButton.disabled = false;
      }
    };
    const finalSymbolsReel1 = [finalGrid[0][0], finalGrid[1][0], finalGrid[2][0]];
    const finalSymbolsReel2 = [finalGrid[0][1], finalGrid[1][1], finalGrid[2][1]];
    const finalSymbolsReel3 = [finalGrid[0][2], finalGrid[1][2], finalGrid[2][2]];
    animateReelDown(reel1Inner, finalSymbolsReel1, 2, reelFinished);
    animateReelDown(reel2Inner, finalSymbolsReel2, 2.5, reelFinished);
    animateReelDown(reel3Inner, finalSymbolsReel3, 3, reelFinished);
  };

  spinButton.addEventListener('click', spin);

  withdrawButton.addEventListener('click', () => {
    const withdrawalAmount = 625000;
    if (credits < withdrawalAmount) {
      messageDiv.textContent = "You need at least $25 to withdraw.";
      return;
    }

    credits -= withdrawalAmount;
    updateCreditsDisplay();
    messageDiv.textContent = `You have withdrawn $25. Please email support@randoms.top with a screenshot attached and your ID number: ${userID} to complete the withdrawal.`;
  });

  // Add logic for reset button
  resetButton.addEventListener('click', () => {
    credits = config.initialCredits; // Reset credits to initial value
    localStorage.setItem('credits', credits); // Store in local storage
    updateCreditsDisplay(); // Update the display
    messageDiv.textContent = "Credits have been reset!";
  });
}
