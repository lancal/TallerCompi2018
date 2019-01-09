ent notaTaller;
ent promedio;
ent notaTaller1;
ent notaTaller2;
ent notaTaller3;
ent notaTaller4;


ent promedioTaller[ent notaTaller1, ent notaTaller2, ent notaTaller3, ent notaTaller4](

	RET 00;
)

ent main[ent k](

	notaTaller1 = 60;
	notaTaller2 = 40;
	notaTaller3 = 55;
	notaTaller4 = 10;

	promedio = promedioTaller[notaTaller1, notaTaller2, notaTaller3, notaTaller4];

)