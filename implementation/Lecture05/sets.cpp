#include <stddef.h> // library for NULL
//
void create(settype *s)
{
    s->head = NULL ;
    s->size = 0 ;
}

//return 0 if exist
//return 1 if added
int AddElement(settype *s, Entrytype element )
{
    Node * pn = (Node *)malloc(sizeof(Node));
    pn->info = element;

    Node *q = s->head;
    if(!q || q->info > element) //if has no node || if first node
    {
        pn->next = q;
        s->head = pn;
        s->size++;
        return 1;
    }
    while(q->next && q->next->info <= element)
    {
        q = q->next;
    }
    if(q->info == element)
        return 0;
    pn->next = q->next;
    q->next = pn;
    s->size++;
    return 1 ;
}

// return 0 if the element doesn't exist
//return 1 if exist and removed
int SubtractElement(settype *s, Entrytype element )
{
    if(!s->head)
        return 0;

    Node *q = s->head;
    if(q->info == element)
    {
        s->head = q->next ;
        free(q);
        s->size--;
        return 1;
    }
    while(q->next && q->next->info < element)
    {
        q = q->next;
    }
    if(q->next && q->next->info == element)
    {
        Node *pn = q->next;
        q->next = pn->next ;
        free(pn);
        s->size--;
        return 1;
    }
    return 0;
}

int SubtractSet(settype *s1, settype *s2 )
{
    Node *p = s2->head;
    while(p)
    {
        SubtractElement(s1,p->info);
        p = p->next ;
    }
    return 1 ;
}


// s3 is the union of s1 and s2
int Union(settype *s1, settype *s2, settype *s3 )
{
    Node *p = s1->head;
    while(p)
    {
        AddElement(s3,p->info);
        p = p->next ;
    }
    p = s2->head;
    while(p)
    {
        AddElement(s3,p->info);
        p = p->next ;
    }
    return 1 ;
}

int Intersection(settype *s1, settype *s2, settype *s3 )
{
    Node * p = s1->head;
    while(p)
    {
        if(is_in_set(s2,p->info))
            AddElement(s3,p->info);
        p = p->next ;
    }
    return 1 ;
}
// size of set
int cardinality(settype *s)
{
    int size = 0;
    Node *p = s->head;
    while(p)
    {
        size++;
        p = p->next ;

    }
    return size ;
}


int is_in_set(settype *s, Entrytype e )
{
    Node *p = s->head;
    while(p)
    {
        if(p->info == e)
            return 1;
        p = p->next ;
    }
    return 0 ;
}


void display(settype *s)
{
    Node *p = s->head;

    printf("\n**************************************************\n");
    printf("The Data of Set is : \n");
    while(p)
    {
        printf("%d\n",p->info);
        p = p->next ;
    }
    printf("**************************************************\n");
}
