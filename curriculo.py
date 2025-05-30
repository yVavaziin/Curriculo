dados = {
    "nome": "Vagner da Silva",
    "resumo": "Profissional formado em Ciências Contábeis e estudante de Análise e Desenvolvimento de Sistemas.",
    "formacoes": [
        "Ciências Contábeis - Universidade XYZ - Concluído em 2022",
        "Análise e Desenvolvimento de Sistemas - Universidade ABC - Em andamento"
    ],
    "experiencias": [
        "STF - Supremo Tribunal Federal (2020 - 2023) - Estagiário em área administrativa e de dados"
    ],
    "habilidades": ["Python", "HTML", "CSS", "JavaScript", "SQL", "Excel Avançado"],
    "contato": {
        "email": "seuemail@exemplo.com",
        "telefone": "(99) 99999-9999",
        "linkedin": "linkedin.com/in/seuperfil"
    }
}

html = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Currículo de {dados['nome']}</title>
    <link rel="stylesheet" href="estilo.css">
</head>
<body>
    <div class="container">
        <img src="sua_foto.jpg" alt="Foto de {dados['nome']}" class="foto">
        <h1>{dados['nome']}</h1>
        <p>{dados['resumo']}</p>
        <hr>
        <div class="section">
            <h2>📚 Formação Acadêmica</h2>
            <ul>
                {''.join(f"<li>{f}</li>" for f in dados['formacoes'])}
            </ul>
        </div>
        <div class="section">
            <h2>💼 Experiência Profissional</h2>
            <ul>
                {''.join(f"<li>{e}</li>" for e in dados['experiencias'])}
            </ul>
        </div>
        <div class="section">
            <h2>🛠️ Habilidades</h2>
            <ul>
                {''.join(f"<li>{h}</li>" for h in dados['habilidades'])}
            </ul>
        </div>
        <div class="section">
            <h2>📞 Contato</h2>
            <p>Email: {dados['contato']['email']}</p>
            <p>Telefone: {dados['contato']['telefone']}</p>
            <p>LinkedIn: {dados['contato']['linkedin']}</p>
        </div>
    </div>
</body>
</html>
"""

with open("curriculo_gerado.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Currículo gerado com sucesso!")
