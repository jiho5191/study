#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct TreeNode {
    char word[100];
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;

// 트리 생성 함수
TreeNode* createNode(char* word) {
    TreeNode* newNode = (TreeNode*)malloc(sizeof(TreeNode));
    strcpy(newNode->word, word);
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// 삽입 함수
TreeNode* insertNode(TreeNode* root, char* word) {
    // 트리가 비어있다면 root에 단어 삽입
    if (root == NULL) {
        return createNode(word);
    }

    // 입력받은 단어와 root에 있는 단어 strcmp로 문자열 비교
    int compare = strcmp(word, root->word);

    if (compare < 0) {
        root->left = insertNode(root->left, word);
    }
    else if (compare > 0) {
        root->right = insertNode(root->right, word);
    }

    return root;
}

// 중위 순회 함수
void inorder(TreeNode* root) {
    if (root != NULL) {
        inorder(root->left);        // 왼쪽 서브트리
        printf("%s\n", root->word); // 루트 노드
        inorder(root->right);       // 오른쪽 서브트리
    }
}

// 할당된 메모리 해제 함수
void freeTree(TreeNode* root) {
    if (root != NULL) {
        freeTree(root->left);
        freeTree(root->right);
        free(root);
    }
}

int main() {
    TreeNode* root = NULL;

    root = insertNode(root, "NETWORK");
    root = insertNode(root, "DATA");
    root = insertNode(root, "SYSTEM");
    root = insertNode(root, "PROGRAM");
    root = insertNode(root, "AI");
    root = insertNode(root, "SOFTWARE");
    root = insertNode(root, "DAUM");
    root = insertNode(root, "SOUND");

    /*
                       NETWORK
                    /          |
                 DATA        SYSTEM
                /   |        /
               AI  DAUM   PROGRAM
                                |
                            SOFTWARE
                                |
                              SOUND

    */

    printf("이진 탐색 트리 중위 순회 결과\n");
    inorder(root);

    freeTree(root);

    return 0;
}