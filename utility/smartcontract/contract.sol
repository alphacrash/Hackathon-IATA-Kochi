pragma solidity ^0.4.0;
contract Contract {

    struct Agreement {
        string donator;
        string receiver;
        string contract_details;
    }

    Agreement[] private agreements;

    function addAgreement(string donator, string receiver , string contract_details) public {
        agreements.push(Agreement({
            donator: donator,
            receiver: receiver,
            contract_details : contract_details
        }));
    }

    function checkAgreements(string donator, string receiver) public constant returns (string) {
        for (uint i = 0; i < agreements.length; i++) {
            if (compareStrings(agreements[i].donator, donator) && compareStrings(agreements[i].receiver, receiver)) {
                return agreements[i].contract_details;
            }
        }

        return "Contract Not Found";
    }

    function compareStrings (string a, string b) view returns (bool){
       return keccak256(a) == keccak256(b);
   }
}
