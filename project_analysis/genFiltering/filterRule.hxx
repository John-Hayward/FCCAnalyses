#include "edm4hep/MCParticleCollection.h"

bool filterRule(const edm4hep::MCParticleCollection* inColl) {
	//return false;
	//std::cout << "Initialising variables\n";
	int n_electrons = 0;
	float p_x = 0.;
	float p_y = 0.;
	float p_z = 0.;
	//std::cout << "Variables initialised\n";

	for(const auto& particle: *inColl) {
		//std::cout << "Starting new particle checks\n";
		if (std::abs(particle.getPDG()) == 11 && particle.getGeneratorStatus() == 1) {
			//std::cout << "Final state electron present \n";
			n_electrons++;
			//std::cout << "Now have " << n_electrons << " electrons present\n";
		}

		if (n_electrons > 2) { 
			//std::cout << "More than 2 electrons present";
			return false;}

		if(std::abs(particle.getPDG()) == 12 && particle.getGeneratorStatus() == 1) { //Add electron neutrino momentum
			p_x += particle.getMomentum().x;
			p_y += particle.getMomentum().y;
			p_z += particle.getMomentum().z;
		}
	}

//	std::cout << "All particles checked\n";

	float missing_p=std::sqrt(std::pow(p_x, 2) + std::pow(p_y, 2) + std::pow(p_z, 2));

//	std::cout << "Momentum calculated as " << missing_p << "\n";

	return (missing_p>10 && n_electrons==2);
}
