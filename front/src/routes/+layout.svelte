<script>
	let { children } = $props();
</script>

<nav class="navbar">
	<div class="logo">
		<a href="/">🎬 CineMania</a>
	</div>
	<div class="links">
		<a href="/">Home</a>
		<a href="/movies">Filmes</a>
		<a href="/favorite/movies">Filmes Favoritos</a>
		<a href="/person">Celebridades</a>
		<a href="/favorite/persons">Celebridades Favoritas</a>
	</div>
</nav>

<header class="hero">
	<h1>Bem-vindo ao CineMania</h1>
	<p>Explore o mundo dos filmes e conheça suas celebridades favoritas!</p>
</header>

<main>
	{@render children()}
</main>

<style>
	/* Global Styles */
	:global(body) {
		margin: 0;
		font-family: 'Roboto', sans-serif;
		background-color: #1c1c1c;
		color: #f4f4f9;
	}

	/* Navbar Styles */
	.navbar {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 15px 20px;
		background-color: #333;
		position: sticky;
		top: 0;
		z-index: 1000;
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
	}

	.navbar .logo a {
		color: #ffb400;
		text-decoration: none;
		font-size: 1.5rem;
		font-weight: bold;
	}

	.navbar .links a {
		color: #f4f4f9;
		text-decoration: none;
		margin: 0 10px;
		padding: 8px 15px;
		border-radius: 4px;
		transition: all 0.3s;
	}

	.navbar .links a:hover {
		background-color: #444;
		transform: scale(1.1);
	}

	/* Hero Section */
	.hero {
		background: linear-gradient(135deg, #ff7e5f, #feb47b);
		color: white;
		text-align: center;
		padding: 50px 20px;
		box-shadow: 0 6px 10px rgba(0, 0, 0, 0.2);
	}

	.hero h1 {
		font-size: 2.5rem;
		margin: 0;
	}

	.hero p {
		font-size: 1.2rem;
		margin-top: 10px;
	}

	/* Main Content */
	main {
		padding: 20px;
		animation: fadeIn 0.5s ease-in;
	}

	@keyframes fadeIn {
		from { opacity: 0; }
		to { opacity: 1; }
	}

	/* Responsive Design */
	@media (max-width: 768px) {
		.navbar {
			flex-direction: column;
			align-items: flex-start;
		}

		.navbar .links {
			margin-top: 10px;
		}

		.hero h1 {
			font-size: 2rem;
		}

		.hero p {
			font-size: 1rem;
		}
	}
</style>
