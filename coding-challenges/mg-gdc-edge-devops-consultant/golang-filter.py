import requests

def getSkilledCandidatesInGolang():
    url = "http://xyz.com/candidates"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error en la petición: {e}")
        return

    try:
        data = response.json()
        result = data.get("result", [])
    except ValueError:
        print("Error: Respuesta no es JSON válido")
        return

    skilled_candidates = []
    for candidate in result:
        try:
            skills = [s.lower() for s in candidate.get("skills", [])]
            if "golang" in skills:
                skilled_candidates.append(candidate["name"])
        except Exception as e:
            print(f"Error procesando candidato: {e}")

    print("Candidates Skilled in golang :", skilled_candidates)
    print("Total candidates skilled in golang:", len(skilled_candidates))


# Llamada a la función
getSkilledCandidatesInGolang()
