#include <GL/glut.h>
#include <cmath>
#include <vector>

const int WIDTH = 800;
const int HEIGHT = 800;
const int N = 1000000;

std::vector<bool> is_prime(N, true);

void sieve_of_eratosthenes() {
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i * i < N; ++i) {
        if (is_prime[i]) {
            for (int j = i * i; j < N; j += i) {
                is_prime[j] = false;
            }
        }
    }
}

void draw_point(int x, int y) {
    glVertex2i(x, y);
}

void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    glBegin(GL_POINTS);

    int x = WIDTH / 2;
    int y = HEIGHT / 2;
    int dx = 0;
    int dy = -1;
    int segment_length = 1;
    int segment_passed = 0;

    for (int i = 1; i < N; ++i) {
        if (is_prime[i]) {
            draw_point(x, y);
        }

        if (++segment_passed == segment_length) {
            segment_passed = 0;
            int temp = dx;
            dx = -dy;
            dy = temp;

            if (dy == 0) {
                segment_length++;
            }
        }

        x += dx;
        y += dy;
    }

    glEnd();
    glFlush();
}

void init() {
    glClearColor(0.0, 0.0, 0.0, 0.0);
    glColor3f(1.0, 1.0, 1.0);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0.0, WIDTH, 0.0, HEIGHT);
}

int main(int argc, char** argv) {
    sieve_of_eratosthenes();

    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(WIDTH, HEIGHT);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("Ulam Spiral");
    init();
    glutDisplayFunc(display);
    glutMainLoop();

    return 0;
}