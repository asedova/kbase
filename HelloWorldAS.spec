/*
A KBase module: HelloWorldAS
*/

module HelloWorldAS {
 typedef structure {
        string phrase;
    } InParams;
    typedef structure {
        string phrase;
    } OutParams;
    funcdef printhelloworld(InParams params)
        returns (OutParams) authentication required;
};
