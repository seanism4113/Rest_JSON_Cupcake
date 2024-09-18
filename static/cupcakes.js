const BASE_URL = "http://localhost:5000/api";

// Generate the HTML for the cupcake list items
function generateCupcakeHTML(cupcake) {
	return `<div data-cupcake-id=${cupcake.id}>
                <li>
                    ${cupcake.flavor} | ${cupcake.size} | ${cupcake.rating}
                    <button class=delete-button>X</button>
                </li>
                <img class="cupcake-img" src="${cupcake.image}"
            </div>`;
}

// Populate the cupcakes into the list in index.html
async function showCupcakes() {
	const response = await axios.get(`${BASE_URL}/cupcakes`);

	for (let cupcakeData of response.data.cupcakes) {
		$("#cupcake-list").append($(generateCupcakeHTML(cupcakeData)));
	}
}

// Handle the cupcake form

$("#new-cupcake-form").on("submit", async function (event) {
	event.preventDefault();

	const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {
		flavor: $("#form-flavor").val(),
		size: $("#form-size").val(),
		rating: $("#form-rating").val(),
		image: $("#form-image").val(),
	});

	let newCupcake = $(generateCupcakeHTML(newCupcakeResponse.data.cupcake));
	$("#cupcake-list").append(newCupcake);
	$("#new-cupcake-form").trigger("reset");
});

// Handle deleting a cupcake from the list
$("#cupcake-list").on("click", ".delete-button", async function (event) {
	event.preventDefault();
	let cupcake = $(event.target).closest("div");
	let cupcakeId = cupcake.attr("data-cupcake-id");

	await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
	cupcake.remove();
});

$(showCupcakes);
