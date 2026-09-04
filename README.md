# unittest vs pytest

Exemplo de comparação das bibliotecas de teste **unittest** (nativa do Python) e **pytest** (externa), testando a mesma função `soma(a, b)`.

## Arquivos

- `calculadora.py` — função simples `soma(a, b)` que está sendo testada.
- `test_calculadora_unittest.py` — testes escritos com `unittest`.
- `test_calculadora_pytest.py` — os mesmos testes escritos com `pytest`.
- `requirements.txt` — dependência necessária para rodar os testes com pytest.

## Como rodar

### unittest (não precisa instalar nada)
```bash
python -m unittest test_calculadora_unittest.py -v
```

### pytest (precisa instalar antes)
```bash
pip install -r requirements.txt
pytest -v test_calculadora_pytest.py
```

## Testando uma falha proposital

Para reproduzir a comparação de mensagens de erro mostrada na apresentação,
troque `soma(2, 3), 5` (unittest) ou `soma(2, 3) == 5` (pytest) para `6` e rode
os testes novamente. O `pytest` mostra o valor real de cada variável no
momento da falha; o `unittest` mostra apenas o traceback e a asserção que falhou.

## Trabalho acadêmico

Código feito como parte da Prática 01 - Seminário (professor Reinaldo), comparando duas
bibliotecas de testes unitários da mesma linguagem (Python: unittest e pytest).
