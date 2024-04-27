#include "edm4hep/MCParticleCollection.h"

bool filterRule(const edm4hep::MCParticleCollection* inColl) {
	int n_electrons = 0;
	float p_x = 0.;
	float p_y = 0.;
	float p_z = 0.;

	for(const auto& particle: *inColl) {
		if (std::abs(particle.getPDG()) == 11 && particle.getGeneratorStatus() == 1) {
			n_electrons++;
		}

		if (n_electrons > 2) { return false;}

		if(std::abs(particle.getPDG()) == 12 && particle.getGeneratorStatus() == 1) { //Add electron neutrino momentum
			p_x += particle.getMomentum().x;
			p_y += particle.getMomentum().y;
			p_z += particle.getMomentum().z;
		}
	}

	float missing_p=std::sqrt(std::pow(p_x, 2) + std::pow(p_y, 2) + std::pow(p_z, 2));

	return (missing_p>10 && n_electrons==2);
}
