# INSTRUCCIONES CABALLEROS Y RUFIANES

## HISTORIA:
En 1978, el lógico Raymond Smullyan publicó “¿What’s the name of this book?”, un libro de acertijos lógicos. Entre los acertijos del libro había una clase de acertijos que Smullyan llamó acertijos de "caballeros y rufianes".
En un acertijo de caballeros y rufianes, se proporciona la siguiente información: cada personaje es un caballero o un rufián. Un caballero siempre dirá la verdad: si el caballero dice una oración, entonces esa oración es verdadera. Por el contrario, un rufián siempre mentirá: si un rufián dice una oración, entonces esa oración es falsa.
El objetivo del rompecabezas es, dado un conjunto de frases pronunciadas por cada uno de los personajes, determinar, para cada personaje, si ese personaje es un caballero o un rufián.
Por ejemplo, considere un rompecabezas simple con un solo personaje llamado A. A dice "Soy caballero y rufián".
Lógicamente, podríamos razonar que si A fuera un caballero, entonces esa oración tendría que ser verdadera. Pero sabemos que la oración no puede ser verdadera, porque A no puede ser a la vez caballero y rufián; sabemos que cada personaje es caballero o rufián, pero no ambos. Entonces, podríamos concluir, A debe ser un rufián.
Este puzzle es bastante sencillo. ¡Con más personajes y más oraciones, los puzzles pueden volverse más complicados! Su tarea en este problema es determinar cómo representar estos acertijos utilizando la lógica proposicional, de modo que una IA que ejecute un algoritmo de verificación de modelos (model checking) pueda resolver estos acertijos por nosotros.

## INSTRUCCIONES ESPECÍFICAS
Agregue conocimiento a las bases de conocimiento knowledge0, knowledge1, knowledge2 y knowledge3 para resolver los siguientes acertijos.
	•	Puzzle 0 es el puzzle más sencillo. Contiene un solo personaje, A
	◦	A dice: "Soy tanto caballero como rufián".
	•	El puzzle 1 tiene dos personajes: A y B
	◦	A dice "Ambos somos rufianes"
	◦	B no dice nada.
	•	El rompecabezas 2 tiene dos personajes: A y B.
	◦	A dice: "Somos del mismo tipo".
	◦	B dice “Somos de diferentes clases”.
	•	El rompecabezas 3 tiene tres caracteres: A, B y C.
	◦	A dice: "Soy un caballero". o "Soy un rufián", pero no se sabe cuál de los dos ha dicho.
	◦	B dice "A dijo 'soy un rufián'".
	◦	B entonces dice “C es un rufián”.
	◦	C dice "A es un caballero".
En cada uno de los acertijos anteriores, cada personaje es un caballero o un bribón. Cada oración dicha por un caballero es verdadera, y cada oración dicha por un escudero es falsa.
Una vez que haya completado la base de conocimientos para un problema, debería poder ejecutar python3 puzzle.py para ver la solución al rompecabezas.

## PISTAS:
	•	Para cada base de conocimiento, es probable que desee codificar dos tipos diferentes de información: (1) información sobre la estructura del problema en sí (es decir, información proporcionada en la definición de un rompecabezas de Caballeros y Rufianes), y (2) información sobre lo que los personajes realmente dijeron.
	•	Considere lo que significa si una oración es pronunciada por un personaje. ¿Bajo qué condiciones es verdadera esa oración? ¿Bajo qué condiciones es falsa esa oración? ¿Cómo puede expresar eso como una oración lógica?
	•	Hay múltiples bases de conocimiento posibles para cada rompecabezas que calcularán el resultado correcto. Debe intentar elegir una base de conocimiento que ofrezca la traducción más directa de la información en el rompecabezas, en lugar de realizar un razonamiento lógico por su cuenta. También debe considerar cuál sería la representación más concisa de la información en el rompecabezas.
	◦	Por ejemplo, para el Puzzle0, establecer knowledge0 = ARufian daría como resultado una salida correcta, ya que a través de nuestro propio razonamiento sabemos que A debe ser un rufián. Pero hacerlo iría en contra del espíritu de este problema: el objetivo es que tu IA razone por ti.
No debería necesitar (ni debería) modificar logic.py en absoluto para completar este problema.
