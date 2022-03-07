let grid = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

const canvas_max_width = 300 
const canvas_max_height = 300

const grid_rows_input = document.querySelector("#grid-rows")
const grid_columns_input = document.querySelector("#grid-columns")

let all_paths = {}
let current_bot_path = []

setInterval(() => {
    if (current_bot_path.length > 0) {
        active_node = current_bot_path[0]
        inactivate_all_cells()
        $("#cell-" + active_node).addClass("cell-active")
        current_bot_path.shift()
    }
}, 1000)

function inactivate_all_cells() {
    grid.flat().forEach((item, index) => {
        $("#cell-" + index).removeClass("cell-active")
    })
}

grid_rows_input.value = grid.length
grid_columns_input.value = grid[0].length
make_grid()

const change_shape_form = document.querySelector("#change-shape-form")
change_shape_form.addEventListener("submit", (e) => {
    e.preventDefault()
    const rows = parseInt(grid_rows_input.value)
    const columns = parseInt(grid_columns_input.value)
    
    let new_grid = []
    for(let i = 0; i < rows; i++) {
        new_grid.push([])
        for(let j = 0; j < columns; j++) {
            new_grid[i].push(1)
        }
    }

    grid = new_grid
    make_grid()
});

async function fetch_hamlin_path(grid) {
    return new Promise((resolve, reject) => {
        $.post("/hamlin_path", { "grid": JSON.stringify(grid) }, (data) => {
            resolve(data)
        })
    })
}

async function find_hamlin_path() {
    const loading = document.querySelector(".loading")
    loading.innerHTML = "Calculating...";
    all_paths = await fetch_hamlin_path(grid)
    loading.innerHTML = "";
    current_bot_path = all_paths["max_hamlin_path"]
}

function toggle_cell(x, y) {
    grid[y][x] = grid[y][x] == 1 ? 0 : 1
    render()
}

function render() {
    grid.flat().forEach((item, index) => {
        if (item == 0) {
            $("#cell-" + index).addClass("cell-filled")
        }
        if (item == 1) {
            $("#cell-" + index).removeClass("cell-filled")
        }
    });
}

function make_grid() {
    const canvas = document.querySelector(".canvas")
    canvas.innerHTML = ""
    canvas.style.gridTemplate = "repeat(" + grid.length + ", 1fr) / repeat(" + grid[0].length + ", 1fr)"

    for (let y = 0; y < grid.length; y++) {
        for (let x = 0; x < grid[y].length; x++) {
            const cell = document.createElement("div")
            cell.id = "cell-" + (y * grid[y].length + x)
            cell.classList.add("cell")

            if (grid[0].length >= grid.length) {
                cell.style.width = canvas_max_width / grid[y].length + "px"
                cell.style.height = canvas_max_width / grid[y].length + "px"
            } else {
                cell.style.width = canvas_max_height / grid.length + "px"
                cell.style.height = canvas_max_height / grid.length + "px"
            } 
            
            
            cell.addEventListener("click", () => {
                toggle_cell(x, y)
            })
            canvas.appendChild(cell)
        }
    }
}

