const board_element = document.querySelector('.board')
const n = 8

document.addEventListener('keydown', (e) => {
	if (e.key === 'd') {
		board_element.classList.toggle('showdiffs')
	} else if (e.key === 's') {
		board_element.classList.toggle('showsums')
	} else if (e.key === 'c') {
		board_element.classList.toggle('showcoords')
	}
})

for (let i = 0; i < 8; i++) {
	for (let j = 0; j < 8; j++) {
		const cell = document.createElement('button')
		cell.classList.add('cell')
		cell.innerText = `(${i},${j})`
		const diff = document.createElement('span')
		diff.className = 'diff'
		diff.innerHTML = '&Delta; = ' + (i - j).toString()
		cell.appendChild(diff)
		const sum = document.createElement('span')
		sum.className = 'sum'
		sum.innerHTML = '&Sigma; = ' + (i + j).toString()
		cell.appendChild(sum)
		board_element.appendChild(cell)
		cell.addEventListener('click', () => {
			if (cell.hasAttribute('active')) {
				cell.removeAttribute('active')
			} else {
				cell.setAttribute('active', true)
			}
		})
	}
}
