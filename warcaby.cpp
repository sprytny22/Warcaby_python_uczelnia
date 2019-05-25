#include <iostream>

#define AREASIZE 13
#define WHITE 0
#define BLACK 13

using namespace std;


enum Symbol {
	WH, BL, NONE
};

struct Pawn {
	Symbol symbol;
	bool Move_top;
};

struct Field {
	Field *leftB;
	Field *rightB;
	Field *left_nextToB;
	Field *right_nextToB;

	Field *leftT;
	Field *rightT;
	Field *left_nextToT;
	Field *right_nextToT;

	Pawn *CurrentPawn;
};

Pawn *init(Field [], int);
void init(Field []);
Field *getBeatPawn(Pawn*, Field*&, Field []);
Field *getMovePawn(Pawn*, Field*&, Field []);
void Move(Field*&, Field*&, Field[]);

bool gameOver = false;

int main() {
	bool round = true;

	Field Area[AREASIZE];
	init(Area);

	Pawn *pawnsW = init(Area, WHITE);
	Pawn *pawnsB = init(Area, BLACK);
	Field *CurrentPawn = NULL;
	Field *MovePawn = NULL;

	while (!gameOver) {
		if (CurrentPawn) {
			CurrentPawn = NULL;
		}
		if (round) CurrentPawn = getBeatPawn(pawnsW, MovePawn, Area);
		else CurrentPawn = getBeatPawn(pawnsB, MovePawn, Area);
		if (CurrentPawn) {
			Move(CurrentPawn, MovePawn, Area);
			if (round) {
				round = false;
			}
			else {
				round = true;
			}
		}
		else {
			if (round) CurrentPawn = getMovePawn(pawnsW, MovePawn, Area);
			else CurrentPawn = getMovePawn(pawnsB, MovePawn, Area);
			if (CurrentPawn) {
				Move(CurrentPawn, MovePawn, Area);
				if (round) {
					round = false;
				}
				else {
					round = true;
				}
			}
			else {
				gameOver = true;
			}
		}
	}
	delete[] pawnsB;
	delete[] pawnsW;
}

Pawn *init(Field a_area[], int color) {
	if (color == 0) {
		Pawn *pawns = new Pawn[3];
		pawns[0].Move_top = false;
		pawns[0].symbol = Symbol::WH;
		pawns[1].Move_top = false;
		pawns[1].symbol = Symbol::WH;
		pawns[2].Move_top = false;
		pawns[2].symbol = Symbol::WH;
		a_area[0].CurrentPawn = &pawns[0];
		a_area[1].CurrentPawn = &pawns[1];
		a_area[2].CurrentPawn = &pawns[2];
		return pawns;
	}
	else if (color == 13) {
		Pawn *pawns = new Pawn[3];
		pawns[0].Move_top = true;
		pawns[0].symbol = Symbol::BL;
		pawns[1].Move_top = true;
		pawns[1].symbol = Symbol::BL;
		pawns[2].Move_top = true;
		pawns[2].symbol = Symbol::BL;
		a_area[12].CurrentPawn = &pawns[0];
		a_area[11].CurrentPawn = &pawns[1];
		a_area[10].CurrentPawn = &pawns[2];
		return pawns;
	}
}

Field *getMovePawn(Pawn* pawns, Field*& move, Field area[]) {
	Field *field;
	int counter = 0;
	while (counter < 3) {
		for (int i = 0; i < AREASIZE; ++i) {
			if (area[i].CurrentPawn == pawns) {
				field = &area[i];
				if (field->CurrentPawn->symbol == Symbol::WH) {
					if (field->leftT != NULL) {
						if (field->leftT->CurrentPawn == NULL) {
							move = field->leftT;
							return field;
						}
					}
					if (field->rightT != NULL) {
						if (field->rightT->CurrentPawn == NULL) {
							move = field->rightT;
							return field;
						}
					}
				}
				if (field->CurrentPawn->symbol == Symbol::BL) {
					if (field->leftB != NULL) {
						if (field->leftB->CurrentPawn == NULL) {
							move = field->leftB;
							return field;
						}
					}
					if (field->rightB != NULL) {
						if (field->rightB->CurrentPawn == NULL) {
							move = field->rightB;
							return field;
						}
					}
				}

			}
		}
		pawns++;
		counter++;
	}
	return NULL;
}

Field *getBeatPawn(Pawn* pawns, Field*& move, Field area[]) { 
	Field *field;
	move = NULL;
	int counter = 0;
	while (counter < 3) { 
		for (int i = 0; i < AREASIZE; ++i) {
			if (area[i].CurrentPawn == pawns) {
				field = &area[i];
				if (field->CurrentPawn->symbol == Symbol::WH) { 
					if (field->leftT != NULL) {
						if (field->leftT->CurrentPawn != NULL) {
							if (field->leftT->CurrentPawn->symbol == Symbol::BL) {
								if (field->left_nextToT->CurrentPawn == NULL) {
									move = field->left_nextToT;
									field->leftT->CurrentPawn = NULL;
									return field;
								}
							}
						}
					}
					if (field->rightT != NULL) {
						if (field->rightT->CurrentPawn != NULL) {
							if (field->rightT->CurrentPawn->symbol == Symbol::BL) {
								if (field->right_nextToT->CurrentPawn == NULL) {
									move = field->right_nextToT;
									field->rightT->CurrentPawn = NULL;
									return field;
								}
							}
						}
					}
				}
				else if (field->CurrentPawn->symbol == Symbol::BL) {
					if (field->leftB != NULL) {
						if (field->leftB->CurrentPawn != NULL) {
							if (field->leftB->CurrentPawn->symbol == Symbol::WH) {
								if (field->left_nextToB->CurrentPawn == NULL) {
									move = field->left_nextToB;
									field->leftB->CurrentPawn = NULL;
									return field;
								}
							}
						}
					}
					if (field->rightB != NULL) {
						if (field->rightB->CurrentPawn != NULL) {
							if (field->rightB->CurrentPawn->symbol == Symbol::WH) {
								if (field->right_nextToB->CurrentPawn == NULL) {
									move = field->right_nextToB;
									field->rightB->CurrentPawn = NULL;
									return field;
								}
							}
						}
					}
				}
			}
		}
		pawns++;
		counter++;
	}
	return NULL;
}

void Move(Field *& field1, Field*& field2, Field area[]) {
	field2->CurrentPawn = field1->CurrentPawn;
	field1->CurrentPawn = NULL;
}

void init(Field a_Area[]) { 
	a_Area[0].leftT = &a_Area[3];
	a_Area[0].leftB = NULL;
	a_Area[0].left_nextToT = &a_Area[6];
	a_Area[0].left_nextToB = NULL;
	a_Area[0].rightB = NULL;
	a_Area[0].rightT = NULL;
	a_Area[0].right_nextToB = NULL;
	a_Area[0].right_nextToT = NULL;
	a_Area[0].CurrentPawn = NULL;
	//
	a_Area[1].leftT = &a_Area[4];
	a_Area[1].leftB = NULL;
	a_Area[1].left_nextToT = &a_Area[7];
	a_Area[1].left_nextToB = NULL;
	a_Area[1].rightB = NULL;
	a_Area[1].rightT = &a_Area[3];
	a_Area[1].right_nextToB = NULL;
	a_Area[1].right_nextToT = &a_Area[5];
	a_Area[1].CurrentPawn = NULL;
	//
	a_Area[2].leftT = NULL;
	a_Area[2].leftB = NULL;
	a_Area[2].left_nextToT = NULL;
	a_Area[2].left_nextToB = NULL;
	a_Area[2].rightB = NULL;
	a_Area[2].rightT = &a_Area[4];
	a_Area[2].right_nextToB = NULL;
	a_Area[2].right_nextToT = &a_Area[6];
	a_Area[2].CurrentPawn = NULL;
	//
	a_Area[3].leftT = &a_Area[6];
	a_Area[3].leftB = &a_Area[1];
	a_Area[3].left_nextToT = &a_Area[9];
	a_Area[3].left_nextToB = NULL;
	a_Area[3].rightB = &a_Area[0];
	a_Area[3].rightT = &a_Area[5];
	a_Area[3].right_nextToB = NULL;
	a_Area[3].right_nextToT = NULL;
	a_Area[3].CurrentPawn = NULL;
	//
	a_Area[4].leftT = &a_Area[7];
	a_Area[4].leftB = &a_Area[2];
	a_Area[4].left_nextToT = NULL;
	a_Area[4].left_nextToB = NULL;
	a_Area[4].rightB = &a_Area[1];
	a_Area[4].rightT = &a_Area[6];
	a_Area[4].right_nextToB = NULL;
	a_Area[4].right_nextToT = &a_Area[8];
	a_Area[4].CurrentPawn = NULL;
	//
	a_Area[5].leftT = &a_Area[8];
	a_Area[5].leftB = &a_Area[3];
	a_Area[5].left_nextToT = &a_Area[11];
	a_Area[5].left_nextToB = &a_Area[1];
	a_Area[5].rightB = NULL;
	a_Area[5].rightT = NULL;
	a_Area[5].right_nextToB = NULL;
	a_Area[5].right_nextToT = NULL;
	a_Area[5].CurrentPawn = NULL;
	//
	a_Area[6].leftT = &a_Area[9];
	a_Area[6].leftB = &a_Area[4];
	a_Area[6].left_nextToT = &a_Area[12];
	a_Area[6].left_nextToB = &a_Area[2];
	a_Area[6].rightB = &a_Area[5];
	a_Area[6].rightT = &a_Area[8];
	a_Area[6].right_nextToB = &a_Area[0];
	a_Area[6].right_nextToT = &a_Area[10];
	a_Area[6].CurrentPawn = NULL;
	//
	a_Area[7].leftT = NULL;
	a_Area[7].leftB = NULL;
	a_Area[7].left_nextToT = NULL;
	a_Area[7].left_nextToB = NULL;
	a_Area[7].rightB = &a_Area[4];
	a_Area[7].rightT = &a_Area[9];
	a_Area[7].right_nextToB = &a_Area[1];
	a_Area[7].right_nextToT = &a_Area[11];
	a_Area[7].CurrentPawn = NULL;
	//
	a_Area[8].leftT = &a_Area[11];
	a_Area[8].leftB = &a_Area[6];
	a_Area[8].left_nextToT = NULL;
	a_Area[8].left_nextToB = &a_Area[4];
	a_Area[8].rightB = &a_Area[5];
	a_Area[8].rightT = &a_Area[10];
	a_Area[8].right_nextToB = NULL;
	a_Area[8].right_nextToT = NULL;
	a_Area[8].CurrentPawn = NULL;
	//
	a_Area[9].leftT = &a_Area[12];
	a_Area[9].leftB = &a_Area[7];
	a_Area[9].left_nextToT = NULL;
	a_Area[9].left_nextToB = NULL;
	a_Area[9].rightB = &a_Area[6];
	a_Area[9].rightT = &a_Area[11];
	a_Area[9].right_nextToB = &a_Area[3];
	a_Area[9].right_nextToT = NULL;
	a_Area[9].CurrentPawn = NULL;
	//
	a_Area[10].leftT = NULL;
	a_Area[10].leftB = &a_Area[8];
	a_Area[10].left_nextToT = NULL;
	a_Area[10].left_nextToB = &a_Area[6];
	a_Area[10].rightB = NULL;
	a_Area[10].rightT = NULL;
	a_Area[10].right_nextToB = NULL;
	a_Area[10].right_nextToT = NULL;
	a_Area[10].CurrentPawn = NULL;
	//
	a_Area[11].leftT = NULL;
	a_Area[11].leftB = &a_Area[9];
	a_Area[11].left_nextToT = NULL;
	a_Area[11].left_nextToB = &a_Area[7];
	a_Area[11].rightB = &a_Area[8];
	a_Area[11].rightT = NULL;
	a_Area[11].right_nextToB = &a_Area[5];
	a_Area[11].right_nextToT = NULL;
	a_Area[11].CurrentPawn = NULL;
	//
	a_Area[12].leftT = NULL;
	a_Area[12].leftB = NULL;
	a_Area[12].left_nextToT = NULL;
	a_Area[12].left_nextToB = NULL;
	a_Area[12].rightB = &a_Area[9];
	a_Area[12].rightT = NULL;
	a_Area[12].right_nextToB = &a_Area[6];
	a_Area[12].right_nextToT = NULL;
	a_Area[12].CurrentPawn = NULL;
}
